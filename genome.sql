CREATE TABLE samples (
  id SERIAL PRIMARY KEY,
  external_id TEXT,
  organism TEXT,
  tissue TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE experiments (
  id SERIAL PRIMARY KEY,
  sample_id INTEGER REFERENCES samples(id),
  platform TEXT,
  read_type TEXT,
  run_date DATE
);

CREATE TABLE files (
  id SERIAL PRIMARY KEY,
  experiment_id INTEGER REFERENCES experiments(id),
  file_type TEXT,
  s3_path TEXT,
  checksum TEXT
);

CREATE TABLE qc_results (
  id SERIAL PRIMARY KEY,
  file_id INTEGER REFERENCES files(id),
  tool TEXT,
  status TEXT,
  summary JSONB
);

CREATE TABLE variant_summaries (
  id SERIAL PRIMARY KEY,
  file_id INTEGER REFERENCES files(id),
  total_variants INTEGER,
  snps INTEGER,
  indels INTEGER,
  genes JSONB
);
