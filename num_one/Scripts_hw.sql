-- Отримати всі завдання певного користувача.
select * from tasks t
	where user_id =1;
	

-- Вибрати завдання за певним статусом.
select * from tasks t 
	where status_id = 1;
	

-- Оновити статус конкретного завдання
update tasks 
	set status_id =2
	WHERE status_id =1;


-- Отримати список користувачів, які не мають жодного завдання. 
select id,fullname,email 
from users u 
where id not in (select user_id from tasks t);


-- Додати нове завдання для конкретного користувача
insert into tasks (id, title,description,status_id,user_id)
values(22,'Test title number two','',1,1);


-- Отримати всі завдання, які ще не завершено
select * from tasks t 
where status_id not in (select id from status where name='completed');


-- Видалити конкретне завдання
delete from tasks 
where id=22;


-- Знайти користувачів з певною електронною поштою
select * from users
where email like ('%.com');


-- Оновити ім'я користувача
update users 
set fullname='Fm Radio'
where id =1;


--Отримати кількість завдань для кожного статусу (chatGpt)
SELECT status.name, COUNT(*) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;


-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
select tasks.*
from tasks  
join users on tasks.user_id=users.id 
where  users.email like '%.com';


-- Отримати список завдань, що не мають опису
select * from tasks t 
where description ='';


-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
select users.fullname, tasks.title, tasks.description 
from users
join tasks on users.id =tasks.user_id 
join status on tasks.status_id = status.id
where status.name='in progress';


--Отримати користувачів та кількість їхніх завдань.
SELECT users.id, users.fullname, COUNT(tasks.id) AS tasks_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.fullname;

