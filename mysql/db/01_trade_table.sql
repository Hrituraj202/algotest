CREATE TABLE trade (
    `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `asset` VARCHAR(255) NOT NULL,
    `exchanges` TEXT,
    `profit` DECIMAL(10, 2) NOT NULL,
    `timestamp` VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES user(`id`)
);

CREATE INDEX idx_user_id ON trade (`user_id`);