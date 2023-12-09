import User from "../models/UserModel.js";
import argon2 from "argon2";

export const createUser = async(req, res) => {
    const { name, email, password, confPassword, role } = req.body;

    if (password !== confPassword) {
        return res.status(400).json({ msg: "Password dan Confirm Password tidak cocok" });
    }

    const hashPassword = await argon2.hash(password);

    try {
        await User.create({
            name: name,
            email: email,
            password: hashPassword,
            role: role
        });

        res.status(201).json({ msg: "Register Berhasil" });
    } catch (error) {
        if (error.name === 'SequelizeUniqueConstraintError') {
            return res.status(400).json({ msg: 'Email address is already in use' });
        }

        res.status(400).json({ msg: error.message });
    }
};

export const updateUser = async (req, res) => {
    try {
        // Get the user from the database
        const user = await User.findByPk(req.userId);

        if (!user) {
            return res.status(404).json({ msg: "User not found" });
        }

        // Update user data based on request body
        user.name = req.body.name || user.name;
        user.email = req.body.email || user.email;
        // Add more fields as needed

        // Save the updated user to the database
        await user.save();

        // Respond with the updated user data
        res.status(200).json({
            msg: "User data updated successfully",
            user: {
                uuid: user.uuid,
                name: user.name,
                email: user.email,
                role: user.role
            }
        });
    } catch (error) {
        console.error("Error in updateUser controller:", error);
        return res.status(500).json({ msg: "Internal Server Error" });
    }
};