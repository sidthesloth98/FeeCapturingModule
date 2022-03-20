import motor.motor_asyncio

from bson.objectid import ObjectId



MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.payments

payment_collection = database.get_collection("payments_collection")



# helper
def payment_helper(payment_record) -> dict:
    return {
        "id": payment_record["_id"],
        "student_id": payment_record["student_id"],
        "full_name": payment_record["full_name"],
        "email": payment_record["email"],
    }



# Create a new payment record
async def add_payment_record(payment_record: dict) -> dict:
    payment_record = await payment_collection.insert_one(payment_record)
    new_payment = await payment_collection.find_one({"_id": payment_record.inserted_id})
    return payment_helper(new_payment)