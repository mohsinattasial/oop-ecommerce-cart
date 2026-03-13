# E-Commerce Shopping Cart System

## Project Title
E-Commerce Cart System using Python OOP and Strategy Pattern

## Description
This project implements the core logic of an online shopping cart using Python Object Oriented Programming. 
The cart supports adding products, removing items, calculating subtotal, and applying different discount strategies.

The Strategy Pattern is used so that different pricing strategies can be applied without modifying the cart logic.

## Features
- Add products to cart
- Remove products from cart
- Update product quantities
- Calculate subtotal
- Apply percentage discounts
- Checkout total calculation

## OOP Concepts Used
- **Encapsulation** – Cart items are stored internally and accessed via methods.
- **Abstraction** – PricingStrategy defines a discount interface.
- **Polymorphism** – Different discount strategies implement the same method.
- **Composition** – ShoppingCart contains CartItem objects.
- **Strategy Pattern** – Pricing behavior can be changed at runtime.

## Project Structure

oop-ecommerce-cart/