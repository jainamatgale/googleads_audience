CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('SuperAdmin', 'Admin', 'User') DEFAULT 'User',
    is_active BOOLEAN DEFAULT TRUE,
    mfa_enabled BOOLEAN DEFAULT TRUE,
    first_login BOOLEAN DEFAULT TRUE,
    otp_code VARCHAR(6),
    otp_expiry DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (email, password_hash, role, mfa_enabled, first_login)
VALUES ('super-admin', '$2b$12$Ri3WV2bbu081CDZPmVTfJeZIB4G86kN7euU5EHB6CguPjFNWfurm6', 'superadmin', TRUE, TRUE);

ALTER TABLE users
ADD COLUMN email_address VARCHAR(255) UNIQUE;

UPDATE users
SET email_address = 'jainam.shah@galepartners.com'
WHERE role = 'superadmin';

