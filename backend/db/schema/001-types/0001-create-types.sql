CREATE TYPE types.access_modifier_t AS ENUM (
    'PUBLIC',
    'PROTECTED',
    'PRIVATE'
);

CREATE TYPE types.access_status_t AS ENUM (
    'OK',
    'DENIED'
);

CREATE TYPE types.api_key_t AS ENUM (
    'ADMIN',
    'DEVEL',
    'PUBLIC',
    'PRIVATE'
);

CREATE TYPE types.config_option_t AS ENUM (
    'STRING',
    'INT',
    'NUMERIC',
    'BOOL',
    'DATA'
);

CREATE TYPE types.job_duration_unit_t as ENUM(
    'DAYS',
    'WEEKS',
    'MONTHS',
    'YEARS'
);

CREATE TYPE types.gender_t AS ENUM (
    'MALE',
    'FEMALE',
    'OTHER'
);

CREATE TYPE types.job_type_t AS ENUM (
    'STANDARD',
    'SHORT-TERM',
    'PART-TIME',
    'CONTRACT',
    'OTHER'
);

CREATE TYPE types.syslog_level_t AS ENUM (
    'INFO',
    'WARN',
    'ERROR',
    'DEBUG',
    'ACCESS_VIOLATION'
);

CREATE TYPE types.task_status_t AS ENUM (
    'PENDING',
    'IN_PROGRESS',
    'OK',
    'FAILED',
    'CANCELLED',
    'DROPPED'
);

CREATE TYPE types.user_t AS ENUM (
    'INDIVIDUAL',
    'COMPANY'
);


CREATE TYPE types.post_content_type AS ENUM (
    'TEXT',
    'LINK',
    'IMAGE',
    'VIDEO',
    'AUDIO',
    'DOCUMENT'
);

CREATE TYPE types.post_kill_reason AS ENUM (
    'DUPLICATE',
    'SPAM',
    'FALSE',
    'INVALID',
    'OTHER'
);

