import json
import sys
import os
verbose = False
def init():
    if verbose:
        print("Initializing")
    project = {}
    project_name = input("Enter project name:")
    if project_name == "":
        print("Project name cannot be empty")
        sys.exit(1)
    project_description = input("Enter project description:")
    project_version = input("Enter project version:")
    if project_version == "":
        print("Project version cannot be empty it is set to 1.0.0")
        project_version = "1.0.0"
    project_author = input("Enter project author:")
    project_license = input("Enter project license:")
    project_url = input("Enter project url:")
    project_email = input("Enter project email:")
        
    
    project["name"] = project_name
    project["description"] = project_description
    project["version"] = project_version
    project["author"] = project_author
    project["license"] = project_license
    project["url"] = project_url
    project["email"] = project_email
    print("\nAuto scanning for languages in the project")
    project["languages"] = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py") or file.endswith(".pyw"):
                if "python" in project["languages"]:
                    pass
                else:
                    project["languages"].append("python")
            elif file.endswith(".java"):
                if "java" in project["languages"]:
                    pass
                else:
                    project["languages"].append("java")
            elif file.endswith(".c"):
                if "c" in project["languages"]:
                    pass
                else:
                    project["languages"].append("c")
            elif file.endswith(".cpp"):
                if "c++" in project["languages"]:
                    pass
                else:
                    project["languages"].append("c++")
            elif file.endswith(".h"):
                if "c++" in project["languages"]:
                    pass
                else:
                    project["languages"].append("c++")
            elif file.endswith(".sh"):
                if "shell" in project["languages"]:
                    pass
                else:
                    project["languages"].append("shell")
            elif file.endswith(".js"):
                if "javascript" in project["languages"]:
                    pass
                else:
                    project["languages"].append("javascript")
            elif file.endswith(".html"):
                if "html" in project["languages"]:
                    pass
                else:
                    project["languages"].append("html")
            elif file.endswith(".css"):
                if "css" in project["languages"]:
                    pass
                else:
                    project["languages"].append("css")
            elif file.endswith(".ts") or file.endswith(".tsx"):
                if "typescript" in project["languages"]:
                    pass
                else:
                    project["languages"].append("typescript")
            elif file.endswith(".rb") or file.endswith(".rbx"):
                if "ruby" in project["languages"]:
                    pass
                else:
                    project["languages"].append("ruby")
            elif file.endswith(".go") or file.endswith(".golang"):
                if "go" in project["languages"]:
                    pass
                else:
                    project["languages"].append("go")
            elif file.endswith(".php") or file.endswith(".php5"):
                if "php" in project["languages"]:
                    pass
                else:
                    project["languages"].append("php")
    print("\nPlease enter the actions that you want to add to the project")
    print("Leave blank to skip")
    project_run = input("Enter the command to run the project:")
    project_build = input("Enter build commands:")
    project_test = input("Enter test commands:")
    project_install = input("Enter install commands:")
    project_clean = input("Enter clean commands:")
    project["actions"] = {}
    if project_run != "":
        project["actions"]["run"] = project_run
    if project_build != "":
        project["actions"]["build"] = project_build
    if project_test != "":
        project["actions"]["test"] = project_test
    if project_install != "":
        project["actions"]["install"] = project_install
    if project_clean != "":
        project["actions"]["clean"] = project_clean
    if input("Is the infomation correct? (y/n)").upper == "Y" or "YES" or "CORRECT":
        print("Writing to file")
        with open("project.json", "w") as f:
            json.dump(project, f, indent=4)
        print("Done")
    else:
        print("Aborting")
        sys.exit(1)

if __name__ == "__main__":
    for i in sys.argv:
        if i == "init":
           init()
           exit()
        if i == "search":
            print("projects in "+os.getcwd())
            for root, dirs, files in os.walk("."):
                for file in files:
                    if file == "project.json":
                        with open(os.path.join(root, file), "r") as f:
                            project = json.load(f)
                            print("name:"+project["name"]+" version:"+ project["version"]+" location:"+os.path.dirname(os.path.join(root, file)))
        if i == "info":
            print("Project file in "+os.getcwd())
            for root, dirs, files in os.walk("."):
                for file in files:
                    if file == "project.json":
                        with open(os.path.join(root, file), "r") as f:
                            project = json.load(f)
                            print("name:"+project["name"])
                            print("version:"+project["version"])
                            print("description:"+project["description"])
                            print("author:"+project["author"])
                            print("license:"+project["license"])
                            print("url:"+project["url"])
                            print("email:"+project["email"])
                            print("languages:")
                            for language in project["languages"]:
                                print("\t"+language)
                            print("actions:")
                            for action in project["actions"]:
                                print("\t"+action+":"+project["actions"][action])
                            exit()
    else:
        if os.path.isfile("project.json"):
            for i in sys.argv:
                project = json.load(open("project.json"))
                if i in project["actions"]:
                    print("Running "+i)
                    os.system(project["actions"][i])
        else:
            print("project.json not found create one with the command init")
            exit()
        