-- :name find_all_todos :many
select * from todos

-- :name find_todo_by_id :one
select * from todos where id = :id

-- :name update_todo :affected
update todos set title = :title, done = :done where id = :id

-- :name create_todo :insert
insert into todos (title) values (:title)

-- :name get_todo_title :scalar
select title from todos where id = :id

-- :name find_todos_by_title :many
select * from todos where title like :pattern
