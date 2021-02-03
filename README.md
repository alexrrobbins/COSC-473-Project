

Project Management Plan (PMP) 
“Schedule Sheep”
“Because organizing your crew shouldn’t have to feel like herding sheep.”
10 Points: Deadline to submit PMP on D2L: Jan 27 before class time. 
5 Points: Present PMP on Jan 27 during class time. PPT is optional.

Group Members with % of contribution:
1. Alex Robbins: 33%
2. Niko Nuzzo 33%
3. Gavin Homan 33%
Client(s): Event organizers, project managers, and anyone else with a need to distribute detailed schedules to a large group of people.
Proposed System Background
Introduction
The reason for developing this system is to create a readily accessible / shareable schedule that can be used in any setting.
The purpose of this system is to provide a fully customizable and detailed schedule that users may create and share with others.
This is a medium-sized system that will dependent on as few APIs as possible. This system is all-purpose meaning anyone can use it. It can be used in a business or educational environment.
The objective of this project is to create events on a schedule that can be easily customized and shared. The success criteria is to add 1-2 working features per sprint and deliver them on time.


Overview
 Current system
Ex: Google Calendar, Outlook, etc.
Schedules are shared with individual people by a central owner. The owner needs to grant access, invite members via email, provide long links with security tokens for those who need to view. The current system forces all viewers of a schedule to create accounts to view a schedule which has been shared to them. This can be frustrating for users who simply want to view a schedule. Another issue with the current system is that viewing a schedule is too complex. An owner needs to invite a viewer via email, which requires a user to have an email account. The viewing links are also usually very long and difficult to remember.
Proposed system
This system will make schedules on a calendar-based format that can be shared with others via a link and passcode. The owner of a schedule will need to create an account to customize and share their schedule. Guests will not need an account to view a schedule that has been shared with them. Guests will only need the link of the schedule and the passcode.
Functional requirements
Signup and login feature
This feature allows users to create an account/login to the system to manage the schedules they created. It will be responsible for procuring user IDs and passwords and storing them in the database.
Storage feature
This feature will be used to store event data, calendar IDs, and hashed passcodes in the database.
Email feature
This feature will first assist users who wish to create schedules by allowing the users to create accounts and verify the email address. It will also allow schedule owners to invite other users to view the schedule.
A future feature would allow guests with access to a schedule to download it in a calendar format for use with other applications.
Schedule feature
This feature will associate schedules with their owners as well as a schedule’s unique ID which will be present in its URL, the passcode to access the schedule, and the events that make it up. 
Event feature
Add / Edit / Delete events. The schedule owner will have the ability to perform these actions. This feature provides the primary functionality of the system. The events will have a start and end time as well as a location.
Guest feature
This feature will allow people to view the schedule of others. This feature will be responsible for getting the unique ID of the schedule from the viewer and the passcode from the viewer. It will then bring up the requested schedule to display to the viewer. 
Search feature
This feature will allow guests viewing the calendar to search for events by keywords, dates, or times. It will also give the same functionality to the owner of the schedule.
View/Style
A component of the project must be present and responsible for providing the view of the project. It will give the application its appearance and style for all users. 


Nonfunctional requirements
The system should be straightforward to use and not present a variety of obstacles to the user. What that means is the steps that a user needs to take to accomplish a task should be minimal. 
The system should be responsive, but not necessarily provide real-time (split-second) interaction. This means that the system should be efficient enough to fulfill a request in less than 5 seconds, which is a reasonable wait time. 
The system should be secure in the sense that unauthorized access to user accounts and private schedules should be prohibited. The system design should keep confidentiality, integrity, and accessibility in mind. The website should not be prone to any common vulnerabilities such as SQL injection, XSS, and the usage of unhashed passwords.
The application should be testable and the results should be verifiable in every step of its development.
The application will use the model-view-controller infrastructure to maintain separation of duties between the web browser, the backend logic, and the database. This approach should also boost security and maintainability.
Hardware requirements
The system will be hosted on a Linux-based server and will need roughly 200GB of storage for hosting the system and providing basic storage for the database. Since this project will not be used on a large scale, basic system requirements should suffice (at least 8 GB of RAM and a respectable CPU).
System models
Context diagram

 


Use case model and use case descriptions




