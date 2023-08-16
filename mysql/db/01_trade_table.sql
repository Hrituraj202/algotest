CREATE TABLE trade (
    `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `asset` VARCHAR(255) NOT NULL,
    `exchanges` JSON,
    `profit_percent` DECIMAL(10, 2) NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,
    CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES user(`id`)
);

CREATE INDEX idx_user_id ON trade (`user_id`);