-- convert database
-- to utf

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table MODIFY namee VARCHAR(255) CHARACTER SET utf8;
