from distutils.core import setup

setup(name="Scene Fuser", 
 version="1.0", 
 description="Fusiona tus colecciones de escenas de OBS", 
 author="Jaime", 
 author_email="jaimefa00@gmail.com", 
 url="url del proyecto", 
 license="tipo de licencia", 
 scripts=["script.py"], 
 console=["script.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)