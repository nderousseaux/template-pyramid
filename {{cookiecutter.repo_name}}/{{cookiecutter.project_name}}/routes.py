def includeme(config):
    config.add_route("home", "/")
    
    config.scan(".views")
