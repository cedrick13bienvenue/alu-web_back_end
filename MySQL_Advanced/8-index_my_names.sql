-- Creates an index on the first letter of names.name
CREATE INDEX idx_name_first ON names (name(1));
