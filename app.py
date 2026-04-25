from datetime import datetime
from pathlib import Path
import os
import sqlite3
import uuid

from flask import Flask, abort, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.getenv("DATABASE_PATH", str(BASE_DIR / "board.db")))
UPLOAD_DIR = Path(os.getenv("UPLOAD_FOLDER", str(BASE_DIR / "static" / "uploads")))
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                image_path TEXT,
                created_at TEXT NOT NULL
            )
            """
        )

        columns = {
            row[1]
            for row in conn.execute("PRAGMA table_info(post)").fetchall()
        }
        if "image_path" not in columns:
            conn.execute("ALTER TABLE post ADD COLUMN image_path TEXT")
            conn.commit()


def save_uploaded_image(current_image_path: str | None = None) -> tuple[str | None, str | None]:
    image_file = request.files.get("image")
    if image_file is None or image_file.filename == "":
        return current_image_path, None

    filename = secure_filename(image_file.filename)
    extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if extension not in ALLOWED_EXTENSIONS:
        return current_image_path, "이미지 파일은 png, jpg, jpeg, gif, webp만 업로드할 수 있습니다."

    image_file.stream.seek(0, 2)
    file_size = image_file.stream.tell()
    image_file.stream.seek(0)
    if file_size > MAX_IMAGE_SIZE_BYTES:
        return current_image_path, "이미지 크기는 최대 5MB까지 업로드할 수 있습니다."

    stored_name = f"{uuid.uuid4().hex}.{extension}"
    destination = UPLOAD_DIR / stored_name
    image_file.save(destination)
    return f"uploads/{stored_name}", None


@app.route("/")
def root() -> str:
    return redirect(url_for("post_list"))


@app.route("/posts")
def post_list() -> str:
    with get_db_connection() as conn:
        posts = conn.execute(
            "SELECT id, title, content, image_path, created_at FROM post ORDER BY id DESC"
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
                    form_action=url_for("post_new"),
                    submit_label="Publish",
                    page_title="글쓰기",
                    image_path=None,
                ),
                400,
            )

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        image_path, upload_error = save_uploaded_image()
        if upload_error:
            return (
                render_template(
                    "new.html",
                    error=upload_error,
                    title=title,
                    content=content,
                    form_action=url_for("post_new"),
                    submit_label="Publish",
                    page_title="글쓰기",
                    image_path=None,
                ),
                400,
            )

        with get_db_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO post (title, content, image_path, created_at) VALUES (?, ?, ?, ?)",
                (title, content, image_path, created_at),
            )
            post_id = cursor.lastrowid
            conn.commit()

        return redirect(url_for("post_detail", post_id=post_id))

    return render_template(
        "new.html",
        error=None,
        title="",
        content="",
        form_action=url_for("post_new"),
        submit_label="Publish",
        page_title="글쓰기",
        image_path=None,
    )


@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def post_edit(post_id: int) -> str:
    with get_db_connection() as conn:
        post = conn.execute(
            "SELECT id, title, content, image_path FROM post WHERE id = ?",
            (post_id,),
        ).fetchone()

    if post is None:
        abort(404)

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
                    form_action=url_for("post_edit", post_id=post_id),
                    submit_label="Update",
                    page_title="글 수정",
                    image_path=post["image_path"],
                ),
                400,
            )

        image_path, upload_error = save_uploaded_image(post["image_path"])
        if upload_error:
            return (
                render_template(
                    "new.html",
                    error=upload_error,
                    title=title,
                    content=content,
                    form_action=url_for("post_edit", post_id=post_id),
                    submit_label="Update",
                    page_title="글 수정",
                    image_path=post["image_path"],
                ),
                400,
            )

        with get_db_connection() as conn:
            conn.execute(
                "UPDATE post SET title = ?, content = ?, image_path = ? WHERE id = ?",
                (title, content, image_path, post_id),
            )
            conn.commit()

        return redirect(url_for("post_detail", post_id=post_id))

    return render_template(
        "new.html",
        error=None,
        title=post["title"],
        content=post["content"],
        form_action=url_for("post_edit", post_id=post_id),
        submit_label="Update",
        page_title="글 수정",
        image_path=post["image_path"],
    )


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def post_delete(post_id: int) -> str:
    with get_db_connection() as conn:
        conn.execute("DELETE FROM post WHERE id = ?", (post_id,))
        conn.commit()

    return redirect(url_for("post_list"))


@app.route("/posts/<int:post_id>")
def post_detail(post_id: int) -> str:
    with get_db_connection() as conn:
        post = conn.execute(
            "SELECT id, title, content, image_path, created_at FROM post WHERE id = ?",
            (post_id,),
        ).fetchone()

    if post is None:
        abort(404)

    return render_template("detail.html", post=post)


init_db()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1",
    )
