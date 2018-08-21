CREATE TABLE core.tasks (
    id bigserial primary key,
    resource character varying(255) NOT NULL,
    input_data text,
    result_data text,
    status types.task_status_t DEFAULT 'PENDING'::types.task_status_t,
    ctime timestamp without time zone DEFAULT now() NOT NULL,
    mtime timestamp without time zone DEFAULT now() NOT NULL,
    origin_node character varying(255) NOT NULL,
    worker_node character varying(255) DEFAULT NULL::character varying,
    error text
);

CREATE INDEX tasks_resource_idx ON core.tasks USING btree (resource);

CREATE TRIGGER trg_update_mtime BEFORE INSERT OR UPDATE ON core.tasks
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_update_mtime();
