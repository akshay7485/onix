FROM nginx:latest
COPY . /usr/share/nginx/html
# Expose port 80
EXPOSE 80

# Start Nginx

