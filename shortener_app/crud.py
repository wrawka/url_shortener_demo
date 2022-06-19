# shortener_app/crud.py

from sqlalchemy.orm import Session

from . import keygen, models, schemas


def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )


def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    """Create new short URL database record."""
    key = keygen.create_unique_random_key(db=db)
    secret_key = f"{key}_{keygen.create_random_key(length=8)}"
    db_url = models.URL(target_url=url.target_url, key=key, secret_key=secret_key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_db_url_by_secret_key(db: Session, secret_key: str) -> models.URL:
    """Checks database for an active database entry with the provided `secret_key`."""
    return (
        db.query(models.URL)
        .filter(models.URL.secret_key == secret_key, models.URL.is_active)
        .first()
    )


def update_db_clicks(db: Session, db_url: schemas.URL) -> models.URL:
    """Increment short URL link click counter."""
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)
    return db_url
