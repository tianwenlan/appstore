package com.appstore.service.impl;

import java.util.List;

import com.appstore.dao.AppDAO;
import com.appstore.entity.App;
import com.appstore.service.AppService;

public class AppServImpl implements AppService{

	private AppDAO appDao;
	
	@Override
	public App getApp(App app) {
		// TODO Auto-generated method stub
		return this.appDao.readApp(app);
	}

	@Override
	public List<App> readRecomApps(List<String> appIDs) {
		// TODO Auto-generated method stub
		return this.appDao.readRecomApps(appIDs);
	}

	@Override
	public List<App> readTopNApps() {
		// TODO Auto-generated method stub
		return this.appDao.readTopNApps();
	}

	public AppDAO getAppDao() {
		return appDao;
	}

	public void setAppDao(AppDAO appDao) {
		this.appDao = appDao;
	}
	
}
