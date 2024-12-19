# Start with the Apache image
FROM httpd:2.4

# Copy website files into the container
COPY ./root/onix /usr/local/apache2/htdocs/

# Set up volumes to store actual data outside the container
VOLUME ["/usr/local/apache2/htdocs"]

# Expose port 80 for the web server
EXPOSE 80
