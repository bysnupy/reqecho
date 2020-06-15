from reqecho import echo

echo.run(
    host = '0.0.0.0',
    threaded = True,
    debug = False,
    port = 8080
)
