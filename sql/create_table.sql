create table if not exists TEXT_RUNS (
	ID BIGINT generated always as identity primary key,
	TITLE VARCHAR(80) not null check (LENGTH(TRIM(TITLE))>0),
	SOURCE_TEXT TEXT not null check (LENGTH(TRIM(SOURCE_TEXT))>0),
	CHAR_COUNT INTEGER not null check (CHAR_COUNT>=0),
	WORD_COUNT INTEGER not null check (WORD_COUNT>=0),
	TOP_TOKENS JSONB not null,
	ANALYSIS_VERSION VARCHAR(20) not null,
	REQUEST_KEY UUID unique not null,
	CREATED_AT TIMESTAMPTZ not null default CURRENT_TIMESTAMP
);