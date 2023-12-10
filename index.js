import express from "express";
import cors from "cors";
import session from "express-session";
import dotenv from "dotenv";
import db from "./config/Database.js";
import SequelizeStore from "connect-session-sequelize";
import UserRoute from "./routes/UserRoute.js";
import AuthRoute from "./routes/AuthRoute.js";
import FlowerRoute from "./routes/FlowerRoute.js";

dotenv.config();

const app = express();

const sessionStore = SequelizeStore(session.Store);

const store = new sessionStore({
    db: db
});

(async()=> { await db.sync(); } ) ();

app.use(session({
    secret: process.env.SESS_SECRET,
    resave: false,
    saveUninitialized: true,
    store: store,
    cookie: {
        secure: 'auto'
    }
}));

app.use(cors({
    credentials: true,
    origin: 'http://localhost:3000'
}));
app.use(express.json());
app.use(UserRoute);
app.use(AuthRoute);
app.use(FlowerRoute);

// Root route handler
app.get('/', (req, res) => {
    res.send('Bungaku-API is Active');
});

const port = process.env.APP_PORT || 3000;
app.listen(port, ()=> {
    console.log(`Bungaku-Api Berjalan Pada Port ${port}`);
    
});
