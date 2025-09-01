# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import pickle
import joblib
import numpy as np

app = Flask(__name__)

# Load model (replace with your model path)

model = joblib.load("model_syscalls.pkl")

# List of required syscalls
syscalls = [
    "__arm_nr_cacheflush","__arm_nr_set_tls","_llseek","_newselect","accept","access","bind","brk","capset",
    "chdir","chmod","chown32","clock_getres","clock_gettime","clone","close","connect","dup","dup2","epoll_create",
    "epoll_ctl","epoll_wait","eventfd2","execve","exit","exit_group","faccessat","fchmod","fchown32","fcntl",
    "fcntl64","fdatasync","flock","fork","fstat64","fstatfs64","fsync","ftruncate","ftruncate64","futex",
    "getcwd","getdents64","getegid32","geteuid32","getgid32","getgroups32","getpeername","getpgid","getpid",
    "getppid","getpriority","getresgid32","getresuid32","getrusage","getsockname","getsockopt","gettid",
    "gettimeofday","getuid32","inotify_add_watch","inotify_init","inotify_rm_watch","ioctl","lgetxattr","link",
    "listen","lseek","lstat64","madvise","mkdir","mknod","mlock","mmap2","mount","mprotect","mremap","msync",
    "munlock","munmap","nanosleep","open","pipe","pipe2","poll","prctl","pread64","ptrace","pwrite64","read",
    "readlink","recvfrom","recvmsg","rename","rmdir","rt_sigprocmask","rt_sigtimedwait","sched_get_priority_max",
    "sched_get_priority_min","sched_getparam","sched_getscheduler","sched_setaffinity","sched_setscheduler",
    "sched_yield","sendmsg","sendto","setgid32","setgroups32","setitimer","setpgid","setpriority","setresgid32",
    "setresuid32","setrlimit","setsid","setsockopt","setuid32","shutdown","sigaction","sigaltstack","sigprocmask",
    "sigsuspend","socket","socketpair","stat64","statfs64","symlink","sysinfo","timer_create","timer_settime",
    "truncate","ugetrlimit","umask","uname","unlink","utimes","vfork","wait4","write","writev"
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/manual_input', methods=["GET", "POST"])
def manual_input():
    if request.method == "POST":
        # Collect input frequencies
        features = []
        for s in syscalls:
            value = request.form.get(s, 0)
            features.append(int(value))

        features = np.array(features).reshape(1, -1)

        # Predict using model
        prediction = model.predict(features)[0]
        return render_template("result.html", prediction=prediction)

    return render_template("manual_input.html", syscalls=syscalls)

@app.route('/upload_apk', methods=["POST"])
def upload_apk():
    # Placeholder for APK feature extraction
    file = request.files["apkfile"]
    filename = file.filename
    return f"APK {filename} uploaded. (Feature extraction not implemented yet.)"

if __name__ == "__main__":
    app.run(debug=True)
