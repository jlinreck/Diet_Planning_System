import React from 'react';
import { db } from '../firebase/firebase-config';
import { collection, addDoc, getDoc, updateDoc, deleteDoc, doc } from 'firebase/firestore';

function FirebaseTest() {
  const testCRUDOperations = async () => {
    console.log("Starting Firebase CRUD operations test...");
    
    try {
      // Create a test meal
      const testMeal = {
        name: "Test Meal",
        ingredients: ["Protein", "Vegetables", "Carbs"],
        calories: 500,
        protein: 30,
        carbs: 40,
        fat: 15,
        createdAt: new Date()
      };
      
      // CREATE
      console.log("Testing CREATE operation...");
      const mealsCollection = collection(db, "meals");
      const mealDocRef = await addDoc(mealsCollection, testMeal);
      console.log("Meal document created with ID:", mealDocRef.id);
      
      // READ
      console.log("Testing READ operation...");
      const mealDocSnap = await getDoc(doc(db, "meals", mealDocRef.id));
      
      if (mealDocSnap.exists()) {
        console.log("Meal document data:", mealDocSnap.data());
      } else {
        console.log("No such meal document!");
        throw new Error("Meal document not found - CREATE operation may have failed");
      }
      
      // UPDATE
      console.log("Testing UPDATE operation...");
      const updateData = {
        name: "Updated Test Meal",
        calories: 550,
        ingredients: ["Protein", "Vegetables", "Carbs", "Healthy Fats"],
        updatedAt: new Date()
      };
      
      await updateDoc(doc(db, "meals", mealDocRef.id), updateData);
      console.log("Meal document updated successfully");
      
      // Verify the update
      const updatedMealSnap = await getDoc(doc(db, "meals", mealDocRef.id));
      console.log("Updated meal document data:", updatedMealSnap.data());
      
      // DELETE
      console.log("Testing DELETE operation...");
      await deleteDoc(doc(db, "meals", mealDocRef.id));
      console.log("Meal document deleted successfully");
      
      // Verify the delete
      const deletedMealSnap = await getDoc(doc(db, "meals", mealDocRef.id));
      if (!deletedMealSnap.exists()) {
        console.log("Meal document successfully deleted and verified");
      } else {
        console.log("Meal document still exists - DELETE operation failed");
        throw new Error("DELETE operation failed");
      }
      
      console.log("All CRUD operations completed successfully!");
    } catch (error) {
      console.error("Error during CRUD operations test:", error);
    }
  };

  return (
    <div className="container">
      <h2>Firebase CRUD Test</h2>
      <button 
        className="btn btn-primary"
        onClick={testCRUDOperations}
      >
        Run CRUD Tests
      </button>
      <p>Check the console (F12) for test results</p>
    </div>
  );
}

export default FirebaseTest;