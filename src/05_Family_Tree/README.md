

## Files

- `main.pl`: The Prolog file that defines the family tree and relationships.
- `Dockerfile`: Defines how the Docker container is built.
- `README.md`: Instructions on how to run the project.

## Steps to Run

Follow the instructions below to set up and run the project:




### 1. Build the Docker Image

In your terminal, navigate to the project directory and run the following command to build the Docker image:

```bash
docker build -t prolog_family_tree .
```

This command will build the Docker image with the SWI-Prolog environment and the `family_tree.pl` file.

### 2. Run the Docker Container

After building the Docker image, run the container interactively using:

```bash
docker run -it prolog_family_tree
```

This will start an interactive SWI-Prolog session inside the container with the `family_tree.pl` file loaded.

### 3. Query the Family Tree

Once inside the Prolog interactive shell, you can run queries to interact with the family tree. Some example queries:

- **Find the father of Mahesh**:
  ```prolog
  ?- father(X, mahesh).
  ```

- **Find all siblings of Umesh**:
  ```prolog
  ?- sibling(X, umesh).
  ```

- **Find the grandfather of Swara**:
  ```prolog
  ?- grandfather(X, swara).
  ```

- **Find the children of Ganpat**:
  ```prolog
  ?- parent(ganpat, X).
  ```

### 4. Exit the Prolog Shell

To exit the Prolog shell and stop the container, type:

```prolog
?- halt.
```

### 5. Clean Up (Optional)

After you're done, you can remove the Docker container and image if needed:

- List running containers:
  ```bash
  docker ps -a
  ```

- Remove the stopped container:
  ```bash
  docker rm <container-id>
  ```

- Remove the Docker image:
  ```bash
  docker rmi prolog_family_tree
  ```
