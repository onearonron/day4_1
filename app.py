from datetime import datetime
from pathlib import Path
import sqlite3

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "board.db"


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


@app.route("/")
def root() -> str:
    return redirect(url_for("post_list"))


@app.route("/posts")
def post_list() -> str:
    with get_db_connection() as conn:
        posts = conn.execute(
            "SELECT id, title, content, created_at FROM post ORDER BY id DESC"
        ).fetchall()
    return render_template("list.html", posts=posts)


@app.route("/posts/new", methods=["GET", "POST"])
def post_new() -> str:
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not title or not content:
            return (
                render_template(
                    "new.html",
                    error="제목과 내용을 입력해주세요.",
                    title=title,
                    content=content,
                ),
                400,
            )

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with get_db_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO post (title, content, created_at) VALUES (?, ?, ?)",
                (title, content, created_at),
            )
            post_id = cursor.lastrowid
            conn.commit()

        return redirect(url_for("post_detail", post_id=post_id))

    return render_template("new.html", error=None, title="", content="")


@app.route("/posts/<int:post_id>")
def post_detail(post_id: int) -> str:
    with get_db_connection() as conn:
        post = conn.execute(
            "SELECT id, title, content, created_at FROM post WHERE id = ?",
            (post_id,),
        ).fetchone()

    if post is None:
        abort(404)

    return render_template("detail.html", post=post)


init_db()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
