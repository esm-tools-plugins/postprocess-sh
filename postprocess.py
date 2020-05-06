import os

def postprocess(config):
    pp_method = pp_type = None
    for model in config["general"]["valid_model_names"]:
        if "postprocess" in config[model]:
            for name in config[model]["postprocess"]:
                if "method" in config[model]["postprocess"][name]:
                    pp_method = config[model]["postprocess"][name]["method"]
                if "type" in config[model]["postprocess"][name]:
                    pp_type = config[model]["postprocess"][name]["type"]
                if pp_type == "shell" and pp_method:
                    #try:
                    os.system(pp_method)
                    #except:
                    #    print("Shell execution of command: '" + pp_method + "' failed, please check...")
    return config
                
