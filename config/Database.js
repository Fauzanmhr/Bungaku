import { Sequelize } from "sequelize";

const db = new Sequelize('database_name', 'username', 'password', {
  host: "mysql",
  dialect: "mysql",
  pool: {
    max: 5, // Maximum number of connection in pool
    min: 0, // Minimum number of connection in pool
    acquire: 30000, // The maximum time, in milliseconds, that pool will try to get connection before throwing error
    idle: 10000 // The maximum time, in milliseconds, that a connection can be idle before being released
  },
  logging: false // Disable logging of SQL queries to the console
});

export default db;

