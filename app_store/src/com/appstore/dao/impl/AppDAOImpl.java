package com.appstore.dao.impl;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.appstore.dao.AppDAO;
import com.appstore.entity.App;

public class AppDAOImpl implements AppDAO {
	private SessionFactory sessionFactory; //hibernate
	
	@Override
	@Transactional
	public App readApp(App app) {
		return (App) this.getSession().get(App.class, app.getAppid());
	}

	@Override
	@Transactional
	public List<App> readRecomApps(List<String> appIDs) {
		List<App> apps = new ArrayList<App>();
		
		if(appIDs == null || appIDs.size()==0){
			return apps;
		}
		
		for(String appid : appIDs)
			apps.add((App) this.getSession().get(App.class, appid));
		return apps;
	}
	
	@Override
	@Transactional
	public List<App> readTopNApps() {
		Query query = this.getSession().createQuery("from App app order by app.score desc");
		List<App> apps = (List<App>) query.list();
		return apps;
	}
	
	public Session getSession() {
		return this.sessionFactory.getCurrentSession();
	}

	public SessionFactory getSessionFactory() {
		return sessionFactory;
	}

	public void setSessionFactory(SessionFactory sessionFactory) {
		this.sessionFactory = sessionFactory;
	}
}
