1. Introduction

This prompt outlines the requirements for a software component or application feature that takes a user's birthday as input and returns their corresponding birthstone and zodiac sign. This functionality aims to provide users with quick and easy access to this astrological and cultural information.

2. Goals

To accurately determine and display the birthstone associated with the user's birth month.
To correctly identify and display the zodiac sign based on the user's birth date.
To provide a user-friendly interface for inputting the birth date.
3. User Stories

As a user, I want to be able to enter my birth date (month and day) so that I can find out my birthstone.
As a user, I want to be able to enter my birth date (month and day) so that I can find out my zodiac sign.
As a user, I want the application to clearly display both my birthstone and zodiac sign after I enter my birth date.
As a user, I want the input method for my birth date to be intuitive and easy to use (e.g., dropdown menus, calendar picker, or clear text fields with formatting guidance).
(Optional) As a user, I would like to see a brief description or interesting fact about my birthstone and/or zodiac sign.
4. Functional Requirements

Input: The system must allow the user to input their birth month and day. The year of birth is not required for determining the birthstone and zodiac sign.
Birthstone Calculation: The system must accurately determine the birthstone based on the provided birth month. The following standard birthstone associations should be used:
January: Garnet
February: Amethyst
March: Aquamarine
April: Diamond
May: Emerald
June: Pearl
July: Ruby
August: Peridot
September: Sapphire
October: Opal
November: Topaz1   
1.
charlesfish.co.uk
charlesfish.co.uk
December: Tanzanite
Zodiac Sign Calculation: The system must accurately determine the zodiac sign based on the provided birth month and day, using the standard Western astrological dates:
Aries: March 21 - April 19
Taurus: April 20 - May 20
Gemini: May 21 - June 20
Cancer: June 21 - July 22
Leo: July 23 - August 22
Virgo: August 23 - September 22
Libra: September 23 - October 22
Scorpio: October 23 - November 21
Sagittarius: November 22 - December 21
Capricorn: December 22 - January 19
Aquarius: January 20 - February 18
Pisces: February 19 - March 20
Output: The system must display the determined birthstone name and zodiac sign name to the user.
Error Handling: The system should provide appropriate feedback if the user enters invalid input (e.g., non-numeric values for month or day, or a day that is not valid for the selected month).
5. Non-Functional Requirements

Performance: The calculation and display of the birthstone and zodiac sign should be quick and efficient.
Usability: The user interface should be intuitive and easy to navigate.
Maintainability: The code should be well-organized and easy to understand and update if birthstone or zodiac assignments change in the future (though these are relatively stable).
6. Technical Considerations (Optional)

Specify the preferred programming language or framework (e.g., Python, JavaScript, Java).
Outline any specific libraries or APIs that should be used.
Define the input and output data formats if this is part of a larger system.
7. Success Criteria

Users can successfully input their birth date.
The system accurately identifies and displays the correct birthstone for the given birth month.
The system accurately identifies and displays the correct zodiac sign for the given birth date.
The user interface is deemed easy to use and understand.