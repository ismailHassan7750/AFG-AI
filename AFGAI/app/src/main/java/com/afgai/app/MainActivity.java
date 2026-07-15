package com.afgai.app;

import android.app.Activity;
import android.os.Bundle;
import android.Manifest;
import android.content.Intent;
import android.net.Uri;
import android.webkit.ValueCallback;
import android.webkit.WebView;
import android.webkit.WebSettings;
import android.webkit.WebChromeClient;
import android.webkit.PermissionRequest;
import android.content.pm.PackageManager;

public class MainActivity extends Activity {

    WebView webView;

    private ValueCallback<Uri[]> uploadMessage;
    private static final int FILE_CHOOSER = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (android.os.Build.VERSION.SDK_INT >= 23) {
            requestPermissions(
                new String[]{
                    Manifest.permission.RECORD_AUDIO
                },
                10
            );
        }

        webView = new WebView(this);

        WebSettings settings = webView.getSettings();

        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(true);

        webView.setWebChromeClient(new WebChromeClient(){

            @Override
            public boolean onShowFileChooser(
                    WebView view,
                    ValueCallback<Uri[]> filePathCallback,
                    FileChooserParams params) {

                uploadMessage = filePathCallback;

                Intent intent = params.createIntent();

                startActivityForResult(intent, FILE_CHOOSER);

                return true;
            }


            @Override
            public void onPermissionRequest(PermissionRequest request){

                runOnUiThread(() -> {
                    request.grant(request.getResources());
                });

            }

        });


        webView.loadUrl("file:///android_asset/index.html");

        setContentView(webView);

    }


    @Override
    protected void onActivityResult(
            int requestCode,
            int resultCode,
            Intent data){

        super.onActivityResult(requestCode,resultCode,data);

        if(requestCode == FILE_CHOOSER){

            if(uploadMessage != null){

                Uri[] result = null;

                if(resultCode == RESULT_OK && data != null){

                    result = new Uri[]{
                        data.getData()
                    };

                }

                uploadMessage.onReceiveValue(result);

                uploadMessage = null;

            }

        }

    }

}
