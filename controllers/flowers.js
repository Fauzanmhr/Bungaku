import Flowers from "../models/flowerModel.js";

// Controller to get flower data by name
export const getFlowerByName = async (req, res) => {
  const flowerName = req.params.flowerName;

  try {
    const flower = await Flowers.findOne({
      where: {
        flower_name: flowerName,
      },
    });

    if (!flower) {
      return res.status(404).json({ error: 'Flower not found' });
    }

    return res.status(200).json(flower);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};

// get all flowers
export const getAllFlowers = async (req, res) => {
    try {
      const flowers = await Flowers.findAll();
      return res.status(200).json(flowers);
    } catch (error) {
      console.error(error);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
  };