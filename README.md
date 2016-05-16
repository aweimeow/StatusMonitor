#### What's statuslook
statuslook is a Flask, psutil based project to create a web server for getting system info (CPU, memory, disk, network state, ...)

#### Quick Start
Before start, you have to install flask and psutil first.
```sh
pip install flask
pip install psutil
```
And clone this project
```sh
git clone https://github.com/aweimeow/statuslook.git
```
After you clone this project, you can start it easily by following command
```sh
python main.py
```
It will print token like following,  
if you want to assign token by yourself,  
you can assign token in `statuslook/token`  
and if you dont want to assign token, it will generate a token randomly for you
```sh
TOKEN: f4360d606e675e0f29ea45f0a3202a73
 * Running on http://<your-eth0-ip>:5678/ (Press CTRL+C to quit)
```

#### Access method
```
http://<your-ip>:5678/<token>/<type>/<func>
```
for example, if you want to get cpu_use_percents,  
you can access `http://<your-ip>:5678/<token>/cpu/cpu_use_percents`  
than it will return cpu use info with `json format`  

for more func information, you can take a look in lib and what func we have.  
we have following type information:
 - cpu
 - memory
 - disk
 - network status

Note: we have 2 type address, difference is 's' in end of line.
```
http://<your-ip>:5678/<token>/cpu/cpu_use_percent
http://<your-ip>:5678/<token>/cpu/cpu_use_percents
```
`cpu_use_percent` is for average value,  
`cpu_use_percents` is list all cpu use state


#### Develop
If you want to add some function for others information,  
you can create a py-file in `lib/`,  
and add following code in `main.py`, change 'name' to what you want
```py
@app.route('/%s/name/<func>' % TOKEN)
def name(func):
    result = getattr(lib.name, func)()
    return Response(json.dumps(result), mimetype='application/json')
```

#### Send the pull request
It is very welcome for send PR to me,  
so please send me pull request feel free :)
