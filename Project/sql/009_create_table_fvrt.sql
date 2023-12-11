CREATE TABLE
    IS601_fvrt (
        id INT AUTO_INCREMENT PRIMARY KEY,
        player_fvrt_id INT NOT NULL,
        user_id int not NULL,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY(player_fvrt_id) REFERENCES IS601_Players(id),
        FOREIGN KEY(user_id) REFERENCES IS601_Users(id),
        UNIQUE KEY(player_fvrt_id,user_id)
    );

