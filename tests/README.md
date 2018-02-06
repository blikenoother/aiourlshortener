# Test the `aiourlshortener`

### Check the requirements

- Setup a virtual environment with additional dependencies

    ```bash
    make venv-dev
    ```

- Add your access tokens into the environment

    ```bash
    export AIOURLSHORTENER_GOOGLE="YOUR TOKEN"
    export AIOURLSHORTENER_BITLY="YOUR TOKEN"
    ```

### Run the tests

```bash
make test
```
