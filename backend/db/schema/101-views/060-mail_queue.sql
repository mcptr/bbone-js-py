CREATE OR REPLACE VIEW views.mail_queue AS
    SELECT
	msg.*,
	mq.message_id,
	u.ident,
	mq.delivery_failures,
	mq.delivery_time
	FROM mail.queue mq
	JOIN mail.messages msg ON msg.id = mq.message_id
	JOIN auth.users u ON u.id = mq.recipient_id
	WHERE mq.sent = FALSE;
