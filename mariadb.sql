-- sungjuk table
create table sungjuk(
    sjno int primary key auto_increment,
    name varchar(10) not null,
    kor int default 0,
    eng int default 0,
    mat int default 0,
    tot int default 0,
    avg float default 0,
    grd varchar(2) default '가',
    regdate timestamp default current_timestamp
)