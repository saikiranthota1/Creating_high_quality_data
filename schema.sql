PRAGMA foreign_keys = ON;

CREATE TABLE organizations (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP
);

CREATE TABLE users (
    id TEXT PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    role TEXT,
    created_at TIMESTAMP
);

CREATE TABLE teams (
    id TEXT PRIMARY KEY,
    name TEXT,
    org_id TEXT,
    function TEXT,
    FOREIGN KEY (org_id) REFERENCES organizations(id)
);

CREATE TABLE team_memberships (
    user_id TEXT,
    team_id TEXT,
    PRIMARY KEY (user_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE projects (
    id TEXT PRIMARY KEY,
    name TEXT,
    team_id TEXT,
    type TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE sections (
    id TEXT PRIMARY KEY,
    name TEXT,
    project_id TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE tasks (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    project_id TEXT,
    section_id TEXT,
    assignee_id TEXT,
    parent_task_id TEXT,
    due_date DATE,
    created_at TIMESTAMP,
    completed BOOLEAN,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (assignee_id) REFERENCES users(id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks(id)
);

CREATE TABLE comments (
    id TEXT PRIMARY KEY,
    task_id TEXT,
    user_id TEXT,
    body TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE custom_field_definitions (
    id TEXT PRIMARY KEY,
    name TEXT,
    field_type TEXT,
    project_id TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE custom_field_values (
    task_id TEXT,
    field_id TEXT,
    value TEXT,
    PRIMARY KEY (task_id, field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(id)
);

CREATE TABLE tags (
    id TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE task_tags (
    task_id TEXT,
    tag_id TEXT,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

CREATE TABLE attachments (
    id TEXT PRIMARY KEY,
    task_id TEXT,
    file_name TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);

