create table config2(
    id INTEGER NOT NULL, 
    notification VARCHAR(150), 
    module_code VARCHAR(150), 
    coordinator_id INTEGER,
    lecturer_id INTEGER, 
    student_id INTEGER, 
    earn_credit DOUBLE, 
    status BOOLEAN, 
    grade varchar(1),
    PRIMARY KEY (id), 
    FOREIGN KEY(module_code) REFERENCES module (module_code),
    FOREIGN KEY(coordinator_id) REFERENCES user (id),
    FOREIGN KEY(lecturer_id) REFERENCES user (id),
    FOREIGN KEY(student_id) REFERENCES user (id)
   
);

INSERT INTO config2 (id, notification, module_code, coordinator_id, lecturer_id, student_id, earn_credit, status, grade)
VALUES 
(1, NULL, 'CE201', 11, 2, 4, 12.0, 0, NULL),
(2, NULL, 'CE201', 11, 2, 5, 10.0, 0, NULL),
(3, NULL, 'CE201', 11, 2, 8, NULL, 0, NULL),
(4, NULL, 'CE201', 11, 2, 3, NULL, 0, NULL),
(5, NULL, 'CE201', 11, 2, 4, 12.0, 0, NULL),
(6, NULL, 'CE201', 11, 2, 7, NULL, 0, NULL),
(7, NULL, 'CE205', 11, 9, 3, NULL, 0, NULL),
(8, NULL, 'CE205', 11, 9, 4, NULL, 0, NULL),
(9, NULL, 'CE205', 11, 9, 5, NULL, 0, NULL),
(10, NULL, 'CE205', 11, 9, 6, NULL, 0, NULL),
(11, NULL, 'CE202', 11, 9, 5, NULL, 0, NULL),
(12, NULL, 'CE202', 11, 9, 6, NULL, 0, NULL),
(13, NULL, 'CE202', 11, 9, 8, NULL, 0, NULL),
(14, NULL, 'CE202', 11, 10, 4, 10.0, 0, NULL),
(15, NULL, 'CE202', 11, 10, 8, NULL, 0, NULL),
(16, NULL, 'CE222', 11, 9, 4, NULL, 0, NULL),
(17, NULL, 'CE223', 11, 9, 5, NULL, 0, NULL);

create table notification(
    id INTEGER NOT NULL,
    s_userrole VARCHAR(150),
    s_userid INTEGER,
    r_userrole VARCHAR(150),
    r_userid INTEGER,
    module_code VARCHAR(150),
    PRIMARY KEY (id),
    FOREIGN KEY(s_userid) REFERENCES user (id),
    FOREIGN KEY(r_userid) REFERENCES user (id),
    FOREIGN KEY(module_code) REFERENCES module (module_code)
);

CREATE TABLE "config2"(
    id INTEGER NOT NULL, 
    module_code VARCHAR(150), 
    coordinator_id INTEGER,
    lecturer_id INTEGER, 
    student_id INTEGER, 
    earn_credit DOUBLE, 
    status BOOLEAN, 
    mark DOUBLE,
    PRIMARY KEY (id), 
    FOREIGN KEY(module_code) REFERENCES module (module_code),
    FOREIGN KEY(coordinator_id) REFERENCES user (id),
    FOREIGN KEY(lecturer_id) REFERENCES user (id),
    FOREIGN KEY(student_id) REFERENCES user (id)
   
);

INSERT INTO config2 (id, module_code, coordinator_id, lecturer_id, student_id, earn_credit, status, mark)
VALUES 

(3, 'CE201', 11, 2, 8, NULL, 0, 4),
(4, 'CE201', 11, 2, 3, NULL, 0, 4),
(6, 'CE201', 11, 2, 7, NULL, 0, 4),
(7, 'CE205', 11, 9, 3, NULL, 0, NULL),
(8, 'CE205', 11, 9, 4, NULL, 0, NULL),
(9, 'CE205', 11, 9, 5, NULL, 0, NULL),
(10, 'CE205', 11, 9, 6, NULL, 0, NULL),
(16, 'CE222', 13, 9, 4, NULL, 0, 3),
(17, 'CE223', 13, 9, 5, NULL, 0, 5),
(25, 'CE202', 13, 12, 3, NULL, 0, 1),
(26, 'CE202', 13, 12, 4, NULL, 0, 1),
(27, 'CE223', 13, 12, 8, NULL, 0, 1),
(28, 'CE235', 13, 12, 4, NULL, 0, NULL),
(29, 'CE235', 13, 12, 5, NULL, 0, NULL),
(30, 'CE235', 13, 12, 6, NULL, 0, NULL),
(31, 'CE235', 13, 12, 7, NULL, 0, NULL),
(32, 'CE235', 13, 12, 8, NULL, 0, NULL),
(33, 'CE235', 13, 12, 9, NULL, 0, NULL),
(34, 'CE235', 13, 12, 10, NULL, 0, NULL),
(35, 'CE205', 13, 12, 4, NULL, 0, NULL),
(39, 'CE205', 13, 12, 8, NULL, 0, NULL),
(40, 'CE205', 13, 12, 9, NULL, 0, NULL),
(41, 'CE205', 13, 12, 10, NULL, 0, NULL),
(42, 'CE201', 13, 12, 4, NULL, 0, NULL),
(43, 'CE201', 13, 12, 5, NULL, 0, NULL),
(44, 'CE201', 13, 12, 6, NULL, 0, NULL),
(47, 'CE201', 13, 12, 9, NULL, 0, NULL),
(48, 'CE201', 13, 12, 10, NULL, 0, NULL);

CREATE table gpa2(
    id INTEGER NOT NULL,
    student_id INTEGER,
    module_code VARCHAR(150),
    module_mark DOUBLE,
    gpa DOUBLE,
    PRIMARY KEY (id),
    FOREIGN KEY(student_id) REFERENCES config (student_id)
    FOREIGN KEY(module_code) REFERENCES config (module_code)
    FOREIGN KEY(module_mark) REFERENCES config (mark)
);
