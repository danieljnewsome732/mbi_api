# mbi_api

This API will validate and create Medicare Benefir Numbers according to the Jan 1 2020 standards

## Database

No database yet

## Developing

```console
$ brew update && brew upgrade python

$ ./scripts/run_local.sh 

```
Test in [browser](http://0.0.0.0:3030/)

*If you get errors on the pip install, try:*

```console
$ xcode-select --install   

$ pip3 install psutil 
```

## Auth 

None required at this time

## Testing

```
# All tests
./scripts/test_local.sh

# A specific test file
./scripts/test_local.sh ./mbi_api/tests/functional/test_mbi_controller.py