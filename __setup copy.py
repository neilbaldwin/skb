
from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = "SKB - Synth Kit Builder for Synthstrom Deluge"
  
setup( 
        name ='skb', 
        version ='1.1.0', 
        author ='Neil Baldwin', 
        author_email ='neil.baldwin@mac.com', 
        url ='https://github.com/neilbaldwin', 
        description ='SKB - Synth Kit Builder for Synthstrom Deluge', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                "skb = skb.skb:main"
            ] 
        }, 
        classifiers = [
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ], 
        keywords ='synthstrom deluge utility synth kit builder', 
        install_requires = requirements, 
        zip_safe = False
) 
