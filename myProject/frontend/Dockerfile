# Use an official Node.js image as a base
FROM node:14

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Expose port 3000 and start the frontend server
EXPOSE 3000
CMD ["npm", "start"]
