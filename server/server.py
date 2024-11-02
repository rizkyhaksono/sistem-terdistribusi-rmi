import Pyro4
import os

@Pyro4.expose
class StorageServer:
    def create_file(self, filename):
        try:
            open(filename, 'w').close()
            return f"File '{filename}' created successfully."
        except Exception as e:
            return f"Error creating file '{filename}': {e}"

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return f"File renamed from '{old_name}' to '{new_name}'."
        except Exception as e:
            return f"Error renaming file '{old_name}': {e}"

    def delete_file(self, filename):
        try:
            os.remove(filename)
            return f"File '{filename}' deleted successfully."
        except Exception as e:
            return f"Error deleting file '{filename}': {e}"

    def create_directory(self, dirname):
        try:
            os.makedirs(dirname, exist_ok=True)
            return f"Directory '{dirname}' created successfully."
        except Exception as e:
            return f"Error creating directory '{dirname}': {e}"

    def rename_directory(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return f"Directory renamed from '{old_name}' to '{new_name}'."
        except Exception as e:
            return f"Error renaming directory '{old_name}': {e}"

    def delete_directory(self, dirname):
        try:
            os.rmdir(dirname)
            return f"Directory '{dirname}' deleted successfully."
        except Exception as e:
            return f"Error deleting directory '{dirname}': {e}"

    def list_directory(self, path="."):
        try:
            contents = os.listdir(path)
            return contents
        except Exception as e:
            return f"Error listing directory '{path}': {e}"

def main():
    daemon = Pyro4.Daemon(host="rmi-server", port=4041)
    ns = Pyro4.locateNS(host="rmi-pyro", port=9090)
    uri = daemon.register(StorageServer)
    ns.register("rmi.s3", uri)
    print("RMI Simple Storage Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
