# android_permissions.py - Android权限管理
try:
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    
    def request_android_permissions():
        """请求Android权限"""
        permissions = [
            Permission.RECORD_AUDIO,
            Permission.INTERNET,
            Permission.WAKE_LOCK,
            Permission.VIBRATE,
            Permission.ACCESS_NETWORK_STATE
        ]
        request_permissions(permissions)
        print("✅ Android权限请求完成")
    
    def check_network_connection():
        """检查网络连接"""
        try:
            ConnectivityManager = autoclass('android.net.ConnectivityManager')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            context = PythonActivity.mActivity
            
            cm = context.getSystemService(context.CONNECTIVITY_SERVICE)
            network_info = cm.getActiveNetworkInfo()
            
            return network_info is not None and network_info.isConnected()
        except:
            return True  # 非Android环境默认有网络

except ImportError:
    def request_android_permissions():
        print("⚠️ 非Android环境，跳过权限请求")
    
    def check_network_connection():
        return True  # 非Android环境默认有网络