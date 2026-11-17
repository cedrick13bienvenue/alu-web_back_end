-- Creates an index on the first letter of names.name and names.score
CREATE INDEX idx_name_first_score ON names (name(1), score);
