CREATE TABLE
    IS601_Players (
        id INT AUTO_INCREMENT PRIMARY KEY,
        
        player_id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        team_name VARCHAR(255) NOT NULL,
        face_image_id VARCHAR(255) NOT NULL,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
         UNIQUE KEY `player_id_unique` (`player_id`),
        INDEX `name_index` (`name`),
        INDEX `team_name_index` (`team_name`)
    );

