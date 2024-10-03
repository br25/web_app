<!-- execute database with shell -->
 - docker exec -it todo_app-db-1 psql -U web_app_user -d web_app_db -W

 <!-- backup postgres database command -->
 docker-compose exec db pg_dumpall -U web_app_
user > backup.sql