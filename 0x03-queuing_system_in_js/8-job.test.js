import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

describe("createPushNotificationsJobs", () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("if jobs is not an array passing Number", () => {
    const jobs = 2;
    expect(() => {
      createPushNotificationsJobs(jobs, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing Object", () => {
    const jobs = {};
    expect(() => {
      createPushNotificationsJobs(jobs, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing String", () => {
    const jobs = "Hello";
    expect(() => {
      createPushNotificationsJobs(jobs, queue);
    }).to.throw("Jobs is not an array");
  });
});
