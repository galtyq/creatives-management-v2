# **Creatives Management System - Project Overview**

## **Objective**
A local web application designed to manage advertising creatives (images and headlines) and facilitate their organization, modification, and uploading to an advertising network via API.

## **Core Features**
1. **Campaigns Management**  
   - Fetch campaign data from an advertising network via API.
   - Display campaigns in a structured list.
   - Allow selection of campaigns for uploading creatives.

2. **Images Management**  
   - Sync with a specified local folder to display all images and subfolders.
   - Perform file operations (rename, move, copy, delete) that reflect both in the app and the actual filesystem.
   - Store and manage image metadata (ID, filename, route, tags, category) in a CSV file.

3. **Headlines Management**  
   - Display and manage a list of headlines sourced from a local CSV file.
   - Add, modify, or delete headlines with changes saved in the CSV file.

4. **Uploading New Creatives**  
   - Select campaigns, images, and headlines.
   - Format the selected creatives into the correct structure for API submission.
   - Send the data to the advertising network for publishing.

---

# **Product Requirements Document (PRD)**

## **1. Project Scope**
A local web-based tool to manage creatives (images and headlines) and sync with both a local folder structure and an external advertising API.

## **2. Users**
- **Primary User**: An individual managing advertising creatives, organizing assets, and publishing new campaigns.

## **3. System Components**
### **3.1 Campaigns Page**
- Fetch campaigns via API.
- Display campaigns in a list view.
- Select campaigns for new ad uploads.

### **3.2 Images Page**
- Scan and display images from a specific local directory.
- Reflect file operations (rename, move, delete, copy) in both the app and the filesystem.
- Store and manage metadata in a CSV file.
- Auto-sync changes from the filesystem to the app.

### **3.3 Headlines Page**
- Load and display headlines from a CSV file.
- Add, edit, and delete headlines.
- Save changes directly to the CSV file.

### **3.4 Creative Upload System**
- Allow selection of campaigns, images, and headlines.
- Format creatives for API submission.
- Upload creatives to the advertising network.

---

## **4. Functional Requirements**
### **4.1 Image Management**
- Sync with the filesystem.
- Track metadata in a CSV file.
- Support rename, move, copy, and delete operations.
- Maintain a unique ID for each image.

### **4.2 Headline Management**
- Read and write to a CSV file.
- Allow user modifications.

### **4.3 Campaigns Management**
- Fetch data via API.
- Enable campaign selection.

### **4.4 Creative Uploading**
- Allow selecting creatives.
- Format data correctly.
- Send to the API.

---

## **5. Non-Functional Requirements**
- Local-only operation (no hosting or authentication).
- Lightweight and responsive UI.
- Sync folder structure with real-time updates.

---

# **Folder Structure**
+-- creatives-manager
    |-- backend
    |   |-- api
    |   |-- services
    |   +-- __pycache__
    |-- frontend
    |   |-- public
    |   +-- src
    |       +-- assets
    +-- venv
        |-- Include
        |-- Lib
---

# **Stack Guidelines**
### **1️ Backend (FastAPI for API & File Management)**

#### **Key Technologies**
- **FastAPI** - Handles API routes efficiently.
- **Pandas** - For handling CSV metadata.
- **OS & shutil** - Managing file operations (move, copy, delete).
- **UUID** - Generates unique IDs for images.
- **Requests** - For making API calls to the advertising network.

### **2️ Frontend (React for UI)**

#### **Key Technologies**
- **React** - Core framework.
- **React Query** - Fetch and sync API data efficiently.
- **Tailwind CSS** - Clean UI design.
- **Axios** - API calls.
