DROP TABLE IF EXISTS "student";
DROP TABLE IF EXISTS "item";
DROP TABLE IF EXISTS "checkout";
DROP TABLE IF EXISTS "checkin";

CREATE TABLE IF NOT EXISTS "student" (
        "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"  TEXT NOT NULL UNIQUE,
        "pwd"   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "item" (
        "id"         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"       TEXT NOT NULL,
        "type"       TEXT NOT NULL,
        "status"     TEXT NOT NULL,
        "code"       INTEGER NOT NULL UNIQUE,
        "status_date"TIMESTAMP NOT NULL,
        "student_id" INTEGER,
        FOREIGN KEY(student_id) REFERENCES student(id) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "checkin" (
        "id"        INTEGER PRIMARY KEY AUTOINCREMENT,
        "student_id"INTEGER NOT NULL,
        "item_id"   INTEGER NOT NULL,
        "date_out"  TIMESTAMP NOT NULL,
        "date_in"   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES student(id) ON UPDATE CASCADE,
        FOREIGN KEY(item_id) REFERENCES item(id) ON UPDATE CASCADE
);