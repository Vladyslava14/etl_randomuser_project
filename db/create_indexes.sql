-- для гео- та country analysis
CREATE INDEX idx_users_country ON users(country);
CREATE INDEX idx_users_city ON users(city);

-- для демографії
CREATE INDEX idx_users_gender ON users(gender);
CREATE INDEX idx_users_age ON users(age);

-- для BI-фільтрів
CREATE INDEX idx_users_nationality ON users(nationality);